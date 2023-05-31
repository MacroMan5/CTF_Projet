const express = require('express');
const { exec } = require('child_process');
const router = express.Router();

const challenges = [
  { id: 1, name: 'Automatisation is key', description: 'Dans ce défi, votre tâche est de décoder un message qui a été encodé.', dockerService: 'automatisationiskey' },
  { id: 2, name: 'XOR with 64', description: '...', dockerService: 'xorwith64' },
  { id: 3, name: 'Login Page 1', description: '...', dockerService: 'loginpage' },
  { id: 4, name: 'Login Page 2', description: '...', dockerService: 'loginpage2' },
  { id: 5, name: 'Check The Log', description: '...', dockerService: 'checkthelog' },
  { id: 6, name: 'Stop Brute Force', description: '...', dockerService: ['ssh_victim', 'attacker'] },
];

router.get('/:id/start', (req, res) => {
  const challengeId = req.params.id;
  const challenge = challenges.find(c => c.id == challengeId);

  if (!challenge) {
    res.status(404).send('Challenge non trouvé');
    return;
  }

  const dockerServices = Array.isArray(challenge.dockerService) ? challenge.dockerService : [challenge.dockerService];
  let errors = [];
  dockerServices.forEach(service => {
    exec(`docker-compose up -d ${service}`, (err, stdout, stderr) => {
      if (err) {
        console.error(err);
        console.error('Stdout:', stdout);
        console.error('Stderr:', stderr);
        errors.push(`Erreur lors du démarrage du service ${service}`);
      }
    });
  });

  if(errors.length) {
    res.status(500).send(errors.join('<br/>'));
  } else {
    res.send('Challenge démarré avec succès');
  }
});



module.exports = router;



// Ce code crée un routeur Express qui, pour l'instant, a une seule route.
// Quand vous accédez à /challenges, le serveur renvoie une liste de challenges au format JSON.
