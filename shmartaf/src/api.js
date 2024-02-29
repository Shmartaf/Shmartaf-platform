// import axios from "axios";
// const api = axios.create({
//   baseURL: "http://localhost:8080",
// });
const BASE_URL = "http://localhost:8080";



// const fetchNeeds = () => {
//   fetch(`${BASE_URL}/requirements?skip=0&limit=10`, {
//     method: 'GET',
//     headers: {
//       'Content-Type': 'application/json',
//     },
//     mode: 'cors',
//     redirect: 'follow',
//   })
//     .then((res) => res.json())
//     .then((data) => {
//       console.log(data);
//       return data;
//     })
//     .catch((error) => {
//       console.error('Error:', error);
//     });

// };

export { BASE_URL };
