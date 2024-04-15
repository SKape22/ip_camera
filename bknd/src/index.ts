import fastify, { FastifyInstance, FastifyRequest, FastifyReply } from 'fastify';
import cors from '@fastify/cors';
import dotenv from 'dotenv';
import axios from 'axios';

dotenv.config();

interface PublishRequest {
    url: string;
    name: string;
}

const app: FastifyInstance = fastify({ logger: true });

app.register(cors, {
    origin: 'http://localhost:5173',
    methods: ['GET', 'POST', 'PUT', 'DELETE'],
    allowedHeaders: ['Content-Type'],
    credentials: true,
});

app.post('/publish', async (request: FastifyRequest<{ Body: PublishRequest }>, reply: FastifyReply) => {
    try {
        const { url, name } = request.body;
        console.log(request.body);

        // Create payload for the POST request
        const payload = {
            name: name,
            source: url
        };

        // Make an HTTP POST request to the specified URL
        const configPath = `http://localhost:9997/v3/config/paths/add/${name}`;
        await axios.post(configPath, payload);

        // Return a response
        return { message: 'Payload posted successfully' };
    } catch (error) {
        console.error('Error:', error);
        reply.code(500).send({ error: 'Internal Server Error' });
    }
});

const ADDRESS = '127.0.0.1';
const PORT = '3000';

const listeners = ['SIGINT', 'SIGTERM'];
listeners.forEach((signal) => {
    process.on(signal, async () => {
        await app.close();
        process.exit(0);
    });
});

const start = async () => {
    try {
        await app.listen(parseInt(PORT, 10), ADDRESS);
    } catch (error) {
        app.log.error(error);
        process.exit(1);
    }
};

start();
