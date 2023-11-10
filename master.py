import os
import select
import subprocess

# pip install typer rich


def main(
    unbuffered_child: bool = True,
    sleep: float = 1,
    n: int = 10,
    buffer_size: int = 0,
    text: bool = False,
    blocking: bool = False,
    read_size: int = -1,
):
    env = {"PYTHONUNBUFFERED": unbuffered_child and "1" or "0"}
    command = ["python", "run.py", str(n), str(sleep)]
    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=buffer_size,
        text=text,
        env=env,
    )
    stdout = proc.stdout
    os.set_blocking(stdout.fileno(), blocking)
    while proc.poll() is None:
        if not blocking:
            r, _, _ = select.select((stdout,), (), ())
            if not r:
                print("STOPPING!")
                break
        data = stdout.read(read_size)
        message = data if text else data.decode()
        print(message, end="", flush=True)

    proc.wait()


if __name__ == "__main__":
    import typer

    typer.run(main)
