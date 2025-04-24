import os
from playsound import playsound

def play_audio(file_path: str) -> None:
    """
    Відтворює аудіофайл за вказаним шляхом.
    Args:
        file_path (str): Шлях до аудіофайлу.
    Raises:
        FileNotFoundError: Якщо файл не існує.
        Exception: У разі інших помилок відтворення.
    """
    try:
        # Перевірка наявності файлу
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл {file_path} не знайдено!")

        # Перевірка розширення файлу (додаткова перевірка)
        if not file_path.lower().endswith('.wav'):
            print("Попередження: рекомендовано використовувати .wav файли.")

        # Відтворення звуку
        playsound(file_path)
        print("Аудіо успішно відтворено!")

    except Exception as e:
        print(f"Помилка: {str(e)}")

if __name__ == "__main__":
    # Безпечний шлях з використанням raw-рядка
    sound_path = r'D:\prog\Project playsound\sound.wav'
    play_audio(sound_path)