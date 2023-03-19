import subprocess
from flask import Flask, request

app = Flask(__name__,template_folder="./")

powershell_script_path = './test.ps1'

@app.route('/run_script', methods=['POST'])
def run_script():
    subprocess.run(['powershell.exe', '-File', powershell_script_path])
    return 'Script executed successfully'

if __name__ == '__main__':
    app.run()
