from dataclasses import dataclass
import json

from solidgpt.workskill.skillio import SkillIOParamCategory


@dataclass
class CustomizedSkillDefinition:
    def __init__(self, skill_name, basic_description, instruction, 
                 qa_example, principles, embedding_background_data_list, 
                 input_method : SkillIOParamCategory, output_method : SkillIOParamCategory):
        self.skill_name : str = skill_name
        self.basic_description : str = basic_description
        self.instruction : str = instruction
        self.qa_example : str = qa_example
        self.principles : str = principles
        self.embedding_background_data_list : str = embedding_background_data_list
        self.input_method : str = input_method
        self.output_method : str = output_method

    def toDict(self):
        return {
            "skill_name": self.skill_name,
            "basic_description": self.basic_description,
            "instruction": self.instruction,
            "qa_example": self.qa_example,
            "principles": self.principles,
            "embedding_background_data_list": self.embedding_background_data_list,
            "input_method": self.input_method,
            "output_method": self.output_method
        }