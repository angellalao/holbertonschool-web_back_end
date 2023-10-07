import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  try {
    const [userData, fileData] = await Promise.all([
      signUpUser(firstName, lastName),
      uploadPhoto(fileName)]);
    return [
      { status: 'fulfilled', value: userData },
      { status: 'fulfilled', value: fileData },
    ];
  } catch (error) {
    return [
      { status: 'rejected', value: error.toString() },
      { status: 'rejected', value: error.toString() },
    ];
  }
}
