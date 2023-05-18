const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const firebase = require('firebase-admin');
const serviceAccount = require('./inventario.json');


const app = express();
const port = 3000;

firebase.initializeApp({
    credential: firebase.credential.cert(serviceAccount),
    databaseURL: 'https://inventario-230d8.firebaseapp.com'
})


app.use(cors({ origin: true }));
app.use(bodyParser.json());

// EndPoints

// GET
app.get('/user', async (req, res) => {
    try {
        const snapshot = await firebase.firestore().collection('user').get();
        const user = snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
        res.status(200).json(user)
    } catch (error) {
        console.log(error);
        res.status(500).send(error)
    }
})

app.get('/abiertos', async (req, res) => {
    // console.log('ejecutandose')
    try {
        const snapshot = await firebase.firestore().collection('abiertos').get();
        const abiertos = snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }))
        res.status(200).json(abiertos);
    } catch (error) {
        console.log('error');
        res.status(500).send(error)
    }
})

app.post('/add', async (req, res) => {
    console.log(req.body)
    try {
        const user = req.body;
        const doc = await firebase.firestore().collection('abiertos').add(user);
        res.status(200).json({ id: doc.id, ...doc })
    } catch (error) {
        console.log('dado un error')
        res.status(500).send(error)
    }
})

app.put('/abiertos/:id', async (req, res) => {
    try {
        const id = req.params.id;
        const task = req.body;
        await admin.firestore().collection('abiertos').doc(id).update(task);
        res.status(200).json({ id, ...task });
    } catch (error) {
        console.log(error);
        res.status(500).send(error);
    }
});

app.delete('/abiertos/:id', async (req, res) => {
    try {
        const id = req.params.id;
        await admin.firestore().collection('abiertos').doc(id).delete();
        res.status(204).send();
    } catch (error) {
        console.log(error);
        res.status(500).send(error);
    }
});















app.listen(port, () => {
    console.log('Servidor escuchando en el puerto 3000')
})