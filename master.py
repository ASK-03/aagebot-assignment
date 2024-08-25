import multiprocessing
import subprocess

def run_bot():
    subprocess.run(["python", "bot.py"])

def run_app():
    subprocess.run(["gunicorn", "app:app", "--bind", "0.0.0.0:5000", "--workers", "2"])

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=run_bot)
    p2 = multiprocessing.Process(target=run_app)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
