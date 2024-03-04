// import axios from "axios";
// const api = axios.create({
//   baseURL: "http://localhost:8080",
// });
const BASE_URL = "http://localhost:8080";
const fetchNeeds = () => {
  return fetch(`${BASE_URL}/requirements?skip=0&limit=10`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      return data;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

const fetchSkills = () => {
  return fetch(`${BASE_URL}/certifications?skip=0&limit=10`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      return data;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

const addUser = (user) => {
  return fetch(`${BASE_URL}/users`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(user),
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      return data;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

const addParent = (parent) => {
  return fetch(`${BASE_URL}/parents`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(parent),
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      return data;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

const addBabysitter = (babysitter) => {
  return fetch(`${BASE_URL}/babysitters`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(babysitter),
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      return data;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

const addChildren = (children) => {
  return fetch(`${BASE_URL}/children`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(children),
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      return data;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

const SignUp = (formData) => {
  return fetch(`${BASE_URL}/users/signup`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(formData),
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      return data;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

const fetchParent = (id) => {
  return fetch(`${BASE_URL}/parents/${id}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
  .then((res) => res.json())
  .then((data) => {
      console.log(data);
      return data;
    })
  .catch((error) => {
      console.error("Error:", error);
    });
};

const fetchBabysitterById = (id) => {
  return fetch(`${BASE_URL}/babysitters/${id}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
  .then((res) => res.json())
  .then((data) => {
    console.log(data);
    return data;
  })
  .catch((error) => {
    console.error("Error:", error);
  });
};

export {
  BASE_URL,
  fetchNeeds,
  fetchSkills,
  addUser,
  addParent,
  addBabysitter,
  addChildren,
  SignUp,
  fetchParent,
  fetchBabysitterById,
};
