const express = require('express');
const { exec } = require('child_process');
const router = express.Router();

const challenges = [
  { id: 1, name: 'Automatisation is key', description: 'Dans ce défi, votre tâche est de décoder un message qui a été encodé.', dockerService: 'automatisationiskey' },
  { id: 2, name: 'Challenge 2', description: '...', dockerComposeFile: 'challenge_2.yml' },
    { id: 3, name: 'Challenge 3', description: '...', dockerComposeFile: 'challenge_3.yml' },
    { id: 4, name: 'Challenge 4', description: '...', dockerComposeFile: 'challenge_4.yml' },
    { id: 5, name: 'Challenge 5', description: '...', dockerComposeFile: 'challenge_5.yml' },
    { id: 6, name: 'Challenge 6', description: '...', dockerComposeFile: 'challenge_6.yml' },
];

router.get('/', (req, res) => {
  res.json(challenges);
});

router.get('/:id/start', (req, res) => {
  const challengeId = req.params.id;
  const challenge = challenges.find(c => c.id == challengeId);

  if (!challenge) {
    res.status(404).send('Challenge non trouvé');
    return;
  }
  
  exec(`docker-compose run ${challenge.dockerService}`, (err, stdout, stderr) => {
    if (err) {
      console.error(err);
      console.error('Stdout:', stdout);
      console.error('Stderr:', stderr);
      res.status(500).send('Erreur lors du démarrage du challenge');
      return;
    }
    res.send('Challenge démarré avec succès');
  });
});

module.exports = router;



// Ce code crée un routeur Express qui, pour l'instant, a une seule route.
// Quand vous accédez à /challenges, le serveur renvoie une liste de challenges au format JSON.