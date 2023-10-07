import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const [userResult, fileResult] = await Promise.all([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName)]);

  const userPromise = {
    status: userResult.status === 'fulfilled' ? 'fulfilled' : 'rejected',
    value: userResult.status === 'fulfilled' ? userResult.value : userResult.reason,
  };

  const filePromise = {
    status: fileResult.status === 'fulfilled' ? 'fulfilled' : 'rejected',
    value: fileResult.status === 'fulfilled' ? fileResult.value : fileResult.reason,
  };
  return Promise.resolve([userPromise, filePromise]);
}
