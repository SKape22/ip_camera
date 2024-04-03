import fastify, { FastifyInstance } from 'fastify'
import cors from '@fastify/cors'
import dotenv from'dotenv'

dotenv.config()

const app: FastifyInstance = fastify({ logger: true });

app.register(cors, {
    origin: 'http://localhost:5173',
    methods: ['GET', 'POST', 'PUT', 'DELETE'],
    allowedHeaders: ['Content-Type'],
    credentials: true,
})

const ADDRESS = '0.0.0.0';
const PORT = '3000' 

const listeners = ['SIGINT', 'SIGTERM']
listeners.forEach((signal) => {
  process.on(signal, async () => {
    await app.close()
    process.exit(0)
  })
})

const start = async () => {
    try {
        app.listen({ 
            host: ADDRESS, 
            port: parseInt(PORT, 10) 
        })
    } catch(error) {
        app.log.error(error);
        process.exit(1);
    }
}

start()