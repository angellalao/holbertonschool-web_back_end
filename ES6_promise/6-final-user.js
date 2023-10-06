import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.all([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((results) => {
      results.map((result) => ({
        status: result.status === 'fulfilled' ? 'fulfillied' : 'rejected',
        value: result.status === 'fulfilled' ? result.value : result.reason,
      }));
    });
}
