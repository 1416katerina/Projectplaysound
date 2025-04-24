import os
from playsound import playsound

def play_audio(file_path: str) -> None:
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл {file_path} не знайдено!")

        if not file_path.lower().endswith('.wav'):
            print("Попередження: рекомендовано використовувати .wav файли.")

        playsound(file_path)
        print("Аудіо успішно відтворено!")

    except Exception as e:
        print(f"Помилка: {str(e)}")

if __name__ == "__main__":
    sound_path = r'D:\prog\Project playsound\sound.wav'
    play_audio(sound_path)