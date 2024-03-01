import { Button, Card, MenuItem, Select, Typography } from "@mui/material";
import Box from "@mui/material/Box";
import { useContext, useEffect, useState } from "react";
import { BabysitterContext } from "../context/BabysitterContext";
import { getAll } from "../api/apiService";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const { state, dispatch } = useContext(BabysitterContext);
  const { users } = state;
  const navigate = useNavigate();
  const [role, setRole] = useState("");
  const [selectedUser, setSelectedUser] = useState("");

  const handleChange = (event) => {
    setRole(event.target.value);
  };

  const selectUser = (event) => {
    setSelectedUser(event.target.value);
    dispatch({ type: "SET_USER", payload: event.target.value });
  };

  const fetchData = async (url) => {
    try {
      const response = await getAll(`/${url}`);
      console.log("-----");
      console.log(`${url} response:`);
      console.log(response);
      console.log("-----");
      return response;
    } catch (error) {
      console.error("Error fetching data:", error);
      alert(error.message);
      throw error;
    }
  };

  useEffect(() => {
    const fetchUsers = async () => {
      const response = await fetchData("users");
      dispatch({ type: "SET_USERS", payload: response });
    };

    fetchUsers();
  }, []);

  return (
    <Box
      sx={{
        display: "flex",
        backgroundColor: "#F8F7F1",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        height: "100vh",
      }}>
      <Card
        sx={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          gap: "20px",
          padding: "20px",
          width: 300,
          borderRadius: 2,
          boxShadow: 2,
        }}>
        <Typography variant="h5">Login</Typography>
        <Typography variant="body1">
          Choose role (Babysitter or Parent)
        </Typography>

        <Box>
          <Select
            value={role}
            onChange={handleChange}
            sx={{ width: 200 }}
            size="small">
            <MenuItem value="babysitter">Babysitter</MenuItem>
            <MenuItem value="parent">Parent</MenuItem>
          </Select>
        </Box>
        <Box>
          <Typography variant="body1">Select user</Typography>
          <Select
            value={selectedUser}
            onChange={selectUser}
            sx={{ width: 200 }}
            size="small">
            {users.map((user) => (
              <MenuItem key={user.id} value={user}>
                {user.name}
              </MenuItem>
            ))}
          </Select>
        </Box>
        <Box sx={{ width: 200 }}>
          <Button
            disabled={!selectedUser || !role}
            variant="contained"
            fullWidth
            onClick={() => {
              dispatch({ type: "SET_ROLE", payload: role });
              navigate("/");
            }}>
            Login
          </Button>
        </Box>
      </Card>
    </Box>
  );
};
export default Login;
