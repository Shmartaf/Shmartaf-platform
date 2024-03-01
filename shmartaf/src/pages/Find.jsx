import Box from "@mui/material/Box";
import BabysitterCard from "../components/BabysitterCard/";
import { useContext, useEffect, useState } from "react";
import { BabysitterContext } from "../context/BabysitterContext";
import { getAll } from "../api/apiService";
import { Button } from "@mui/material";
// impport api

// babysitters = api.get("/babysitters)

const Find = () => {
  const { state, dispatch } = useContext(BabysitterContext);
  const { babysitters } = state;
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchBabysitters = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await getAll("/babysitters");
      console.log("response");
      console.log(response);
      dispatch({ type: "SET_BABYSITTERS", payload: response });
      setLoading(false);
    } catch (error) {
      console.error(error);
      setError(error);
      setLoading(false);
    }
  };

  useEffect(() => {
    if (babysitters.length === 0) {
      fetchBabysitters();
    }
  }, []);

  const Content = () => {
    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error: {error.message}</p>;
    if (babysitters.length === 0) {
      return <p>No Babysitters found</p>;
    }

    return (
      <>
        {babysitters.map((babysitter) => (
          <BabysitterCard key={babysitter.id} {...babysitter} />
        ))}
      </>
    );
  };

  return (
    <>
      <Box
        sx={{
          padding: "4px",
          display: "flex",
          justifyContent: "center",
          backgroundColor: "#F8F7F1",
        }}>
        <Button
          variant="text"
          sx={{ textTransform: "none" }}
          size="large"
          onClick={fetchBabysitters}>
          Refresh Babysitters list
        </Button>
      </Box>
      <Box
        sx={{
          display: "flex",
          flexDirection: "row",
          gap: "20px",
          flexWrap: "wrap",
          padding: "20px 10px",
          justifyContent: "center",
          alignItems: "center",
          backgroundColor: "#F8F7F1",
          minHeight: "100vh",
        }}>
        <Content />
      </Box>
    </>
  );
};
export default Find;
