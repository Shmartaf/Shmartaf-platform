import { useState, useEffect } from 'react';
import Box from "@mui/material/Box";
import BabysitterCard from "../components/BabysitterCard";
import { Button } from "@mui/material";
import { fetchBabysitterById } from "../api"; // Assume this is your API call

const Find = () => {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [babysitter, setBabysitter] = useState(null);

  // Simulate getting the babysitter's ID
  const babysitterId = "c194e1fc-2361-4e35-b47a-e81c025b7e0d";

  useEffect(() => {
    const fetchBabysitter = async () => {
      setLoading(true);
      try {
        // Simulated API call to fetch babysitter by ID
        const data = await fetchBabysitterById(babysitterId);
        setBabysitter(data);
        setLoading(false);
      } catch (error) {
        console.error(error);
        setError(error);
        setLoading(false);
      }
    };

    fetchBabysitter();
  }, [babysitterId]);

  return (
    <>
      <Box
        sx={{
          padding: "4px",
          display: "flex",
          justifyContent: "center",
          backgroundColor: "#F8F7F1",
        }}
      >
        <Button
          variant="text"
          sx={{ textTransform: "none" }}
          size="large"
          onClick={() => fetchBabysitterById(babysitterId)}
        >
          Refresh Babysitter Details
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
        }}
      >
        {loading && <p>Loading...</p>}
        {error && <p>Error: {error.message}</p>}
        {babysitter && (
  <BabysitterCard 
    babysitter={babysitter} 
  />
)}
      </Box>
    </>
  );
};

export default Find;
