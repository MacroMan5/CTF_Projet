
<!DOCTYPE html>
<html>
<head>
  <title>Challenges</title>
</head>
<body>
  <h1>Challenges</h1>
  <div id="challenges"></div>

  <script>
    // Fetch the list of challenges from the server
    fetch('/challenges')
      .then(response => response.json())
      .then(challenges => {
        // Get the challenges container
        const challengesDiv = document.getElementById('challenges');

        // For each challenge, create a button and append it to the container
        challenges.forEach(challenge => {
          const button = document.createElement('button');
          button.textContent = `Start Challenge ${challenge.name}`;
          button.onclick = function() {
            // When button is clicked, make a request to start the challenge
            fetch(`/challenges/${challenge.id}/start`);
          };
          challengesDiv.appendChild(button);
        });
      });
  </script>
</body>
</html>
