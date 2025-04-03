import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photo, User]) => {
      console.log(photo.body, User.firstName, User.lastName);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
