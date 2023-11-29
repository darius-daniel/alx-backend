import { createQueue } from "kue";

const queue = createQueue({'name': 'push_notification_code'});
const job = queue.createJob({
    'phoneNumber': '08146240804',
    'message': 'Mobile',
});

job
  .on('failed', () => console.log('Notification job failed'))
  .on('complete', () => console.log('Notification job completed'))
  .on('enqueue', () => console.log(`Notification job created: ${job.id}`));

job.save();
