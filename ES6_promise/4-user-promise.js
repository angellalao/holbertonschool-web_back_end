export default function signUpUser(firstName, lastName) {
  const newPromise = new Promise((resolve) => {
    resolve({ firstName, lastName });
  });
  return newPromise;
}
