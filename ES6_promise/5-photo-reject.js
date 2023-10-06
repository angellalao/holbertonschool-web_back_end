export default function uploadPhoto(fileName) {
  const newPromise = new Promise((resolve, reject) => {
    reject(Error(`${fileName} cannot be processed`));
  });
  return newPromise;
}
