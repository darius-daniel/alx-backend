import { createClient, print } from "redis";
import { promisify } from 'util';

const client = createClient()
  .on("error", (err) => console.log(`Redis client not connected to the server: ${err}`))
  .on('ready', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const getAsync = promisify(client.get).bind(client);
  await getAsync(schoolName).then((reply) => console.log(reply));
}

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

main();
