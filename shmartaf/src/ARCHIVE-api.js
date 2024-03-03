import axios from "axios";
const api = axios.create({
  baseURL: "http://localhost:8080",
});
const skip = 0;
const limit = 10;
const fetchParents = async () => {
  const response = await api.get(`/parents?skip=${skip}&limit=${limit}`);
  return response.data;
};

const parents = await fetchParents();
print(parents);
export { api, parents };
