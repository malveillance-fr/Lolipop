const express = require('express');
const fs = require('fs');
const { exec } = require('child_process');
const app = express();
const port = 3000;

function logError(errorMessage) {
    const logMessage = `${new Date().toISOString()} - Error: ${errorMessage}\n`;
    fs.appendFile('error_log.txt', logMessage, (err) => {
        if (err) throw err;
        console.log("Error logged.");
    });
}

app.get('/start', (req, res) => {
    exec('python Lolipop.py', (err, stdout, stderr) => {
        if (err) {
            const errorMessage = `Error executing Lolipop.py: ${stderr}`;
            logError(errorMessage);
            res.status(500).send("The tool failed to start due to a 'TRACEBACK' error. We recommend reinstalling the tool.\n\nGithub: https://github.com/malveillance-fr/Lolipop");
            return;
        }

        console.log(`Tool started successfully: ${stdout}`);
        res.send("Tool started successfully.");
    });
});

app.get('/', (req, res) => {
    res.send(`
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Lolipop Tool - Status</title>
        </head>
        <body>
            <h1>Welcome to Lolipop Tool</h1>
            <button onclick="startTool()">Start Tool</button>
            <div id="status">Waiting for action...</div>

            <script>
                function startTool() {
                    fetch('/start')
                        .then(response => response.text())
                        .then(data => {
                            document.getElementById('status').innerText = data;
                        })
                        .catch(error => {
                            document.getElementById('status').innerText = 'An error occurred: ' + error;
                        });
                }
            </script>
        </body>
        </html>
    `);
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
