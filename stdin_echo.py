#!/usr/bin/python3
import asyncio
import sys

# adapted from: https://stackoverflow.com/questions/57730010/python-asyncio-subprocess-write-stdin-and-read-stdout-stderr-continuously
async def read_stdout(stdout):
    print('read_stdout')
    while True:
        buf = await stdout.readline()
        if not buf:
            break

        print(f'stdout: { buf }')


async def read_stderr(stderr):
    print('read_stderr')
    while True:
        buf = await stderr.readline()
        if not buf:
            break

        print(f'stderr: { buf }')


async def write_stdin(stdin, what = sys.stdin):
    print('write_stdin')
    print('waiting for input...')
    while True:
        print('reading!')
        line = what.read(1)
        print('got text')
        buf = line.encode()
        #buf = line
        print(f'stdin: { buf }')

        stdin.write(buf)
        await stdin.drain()
        print('waiting for input...')
        #await asyncio.sleep(0.01)
        await asyncio.sleep(0.1)
    print('done waiting...')


async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    await asyncio.gather(
        read_stderr(proc.stderr),
        read_stdout(proc.stdout),
        write_stdin(proc.stdin, sys.stdin))

# because python 3.6 doesn't have asyncio.run()
# THANK YOU https://stackoverflow.com/questions/55590343/asyncio-run-or-run-until-complete
def arun(aw):
    if sys.version_info >= (3, 7):
        return asyncio.run(aw)

    # Emulate asyncio.run() on older versions
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        return loop.run_until_complete(aw)
    finally:
        loop.close()
        asyncio.set_event_loop(None)

if __name__ == "__main__":
    args = sys.argv
    print(args)
    print("Removing first argument")
    del(args[0])

    command_to_run = ' '.join(args)
    print(command_to_run)

    arun(run(command_to_run))
