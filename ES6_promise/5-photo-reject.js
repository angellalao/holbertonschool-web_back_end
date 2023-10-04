export default function uploadPhoto(fileName) {
  const newPromise = new Promise((reject) => {
    reject(Error(`${fileName} cannot be processed`));
  });
  return newPromise;
}
