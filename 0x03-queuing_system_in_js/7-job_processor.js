import { createQueue } from "kue";

const queue = createQueue();
const blacklist = ["4153518780", "4153518781"];

function sendNotification(phoneNumber, message, job, done) {
  let total = 2;
  let remaining = 2;
  let sendInterval = setInterval(() => {
    if (total - remaining <= total / 2) {
      job.progress(total - remaining, total);
    }
    if (blacklist.includes(phoneNumber) === true) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(sendInterval);
    } else if (total === remaining) {
      console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    }
    --remaining || done();
    remaining || clearInterval(sendInterval);
  }, 1000);
};

queue.process("push_notification_code_2", 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
