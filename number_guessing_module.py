from random import randrange

class NumberGuesser:
  def __init__(
      self,
      prompt_text = "I am thinking of a number",
      result_number = randrange(1, 11)
    ):
    self.prompt_text = prompt_text
    self.result_number = result_number
  
  def start_game(self):
    while True:
      user_input = self.prompt_the_user_for_a_number()
      is_correct = self.check_if_user_input_is_the_correct_number(user_input)
      if is_correct:
        break
  
  def prompt_the_user_for_a_number(self):
    return input(self.prompt_text + "\n")

  def check_if_user_input_is_the_correct_number(self, user_input):
    result_text = self.get_result_text_map(user_input)

    if not user_input.isnumeric():
      print(result_text["invalid"])
      return False

    if int(user_input) > self.result_number:
      print(result_text["too_high"])
      return False
    
    if int(user_input) < self.result_number:
      print(result_text["too_low"])
      return False
    
    print(result_text["correct"])
    return True
  

  def get_result_text_map(self, user_input):
    return {
      "too_high": f"Too high! The number is: {self.result_number}\n",
      "too_low": f"Too low! The number is: {self.result_number}\n",
      "invalid": f"{user_input} is not a number! Please enter a valid number!\n",
      "correct": "Correct! You are the best!"
    }