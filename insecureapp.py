import pickle


def load_data(user_data):
  return pickle.loads(user_data)  # Unsafe if user_data comes from an untrusted source.
