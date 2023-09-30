import os
import json
import argparse

from tqdm import tqdm
from utils import *
from configs import *


class AnswerGenerator():
    def __init__(self, args):
        self.args = args

        # load qa dataset
        self.groundTruthLoader = GroundTruthLoader(os.path.join(self.args.data_dir, self.args.question_type))

    def getPrompt(self, question, context):
        if self.args.no_context == "True":
            prompt = "Provide me the answer to the following question:\n"
            prompt += "Question: " + question + "\n"
        
        else:
            prompt = "Provide me the answer to the following question based on the given context:\n"
            prompt += "Question: " + question + "\n"
            prompt += "Context: " + context + "\n"

        return prompt

    def generateAnswers(self):
        # check directories
        if not os.path.exists(self.args.output_dir):
            os.makedirs(self.args.output_dir)

        # create folder for if no context
        if self.args.no_context == "True":
            flag = "no_context"
        else:
            flag = "with_context"
	
        if not os.path.exists(os.path.join(self.args.output_dir, flag)):
            os.makedirs(os.path.join(self.args.output_dir, flag))

        # create output folder for the question type
        if not os.path.exists(os.path.join(self.args.output_dir, flag, self.args.question_type)):
            os.makedirs(os.path.join(self.args.output_dir, flag, self.args.question_type))

        # get json list
        fileNameList = self.groundTruthLoader.fileNameList

        # generate answers
        for i, jsonFile in enumerate(tqdm(fileNameList)):
            with open(os.path.join(self.args.data_dir, self.args.question_type, jsonFile), "r") as f:
                data = json.load(f)

            # get questions
            questions = data["questions"]

            # for each question, generate prompt
            context = data["context"]

            # record answers
            save_data = {'context': context, 'responses': []}

            for question in questions:
                prompt = self.getPrompt(question, context)

                # construct messages
                messages = [{"role": "user", "content": prompt}]

                try:
                    # generate response
                    result = openai.ChatCompletion.create(model=self.args.model, messages=messages)
                    response = result.choices[0]['message']['content']
                    # record the question answer pair as dict
                    save_data['responses'].append({'question': question, 'answer': response})

                except:
                    print("Error in generating response for {}".format(question))
                    continue

            # save answers
            with open(os.path.join(self.args.output_dir, flag, self.args.question_type, jsonFile), "w") as f:
                json.dump(save_data, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--data_dir', type=str, default="./outputs/wiki_qa")
    parser.add_argument('--output_dir', type=str, default="./outputs/wiki_response")
    parser.add_argument('--question_type', type=str, default="COUNT")
    parser.add_argument('--model', type=str, default="gpt-3.5-turbo")
    parser.add_argument('--no_context', type=str, default="False")

    args = parser.parse_args()

    answerGenerator = AnswerGenerator(args)
    answerGenerator.generateAnswers()
