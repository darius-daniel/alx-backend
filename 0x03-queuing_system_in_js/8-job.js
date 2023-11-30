function createPushNotificationsJobs(jobs, queue) {
  if (jobs instanceof Array) {
    for (const job of jobs) {
      queue.createJob('push_notification_code_3', job)
        .on('enqueue', function () {
          console.log(`Notification job created: ${this.id}`);
        })
        .on('complete', function () {
          console.log(`Notification job ${this.id} completed`);
        })
        .on('failed', function (error) {
          console.log(`Notification job ${this.id} failed: ${error}`);
        })
        .on('progress', function (progress) {
          console.log(`Notification job ${this.id} ${progress}% complete`);
        })
        .save();
    }
  } else {
    throw new Error('Jobs is not an array');
  }
}

export default createPushNotificationsJobs;
