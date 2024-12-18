   def eval_example(user_input):
       eval(user_input)  # Contoh penggunaan eval yang tidak aman

   if __name__ == "__main__":
       eval_example("print('Hello, World!')")
