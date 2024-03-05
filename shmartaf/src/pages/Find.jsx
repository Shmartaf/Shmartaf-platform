import { useState, useEffect } from 'react';
import Box from "@mui/material/Box";
import BabysitterCard from "../components/BabysitterCard";
import { Button } from "@mui/material";
import { fetchAllBabysitters, addToFavorites, fetchParent } from "../api"; // Adjusted to fetch all babysitters
import { useAuth } from "../AuthContext";

const Find = () => {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [babysitters, setBabysitters] = useState([]); // Changed to handle multiple babysitters

  useEffect(() => {
    const fetchBabysitters = async () => {
      setLoading(true);
      try {
        const data = await fetchAllBabysitters(); // This function should fetch all babysitters
        setBabysitters(data);
        setLoading(false);
      } catch (error) {
        console.error(error);
        setError(error);
        setLoading(false);
      }
    };

    fetchBabysitters();
  }, []);

  const { user } = useAuth();



  const toggleFavorite = async (babysitterId, isCurrentlyFavorite) => {
    setLoading(true); // Optional: show loading state
    try {
      // Correctly fetch parent information asynchronously
      const parent = await fetchParent(user.id);
      if (isCurrentlyFavorite) {
        // Placeholder for removing from favorites logic
        //const removeFavorite = { parentid: parent.id, babysitterid: babysitterId }
        //await removeFromFavorites(removeFavorite);
      } else {
        // Add to favorites
        const newFavorite = {parentid: parent.id, babysitterid: babysitterId}
        await addToFavorites(newFavorite);
      }
      // Refresh babysitters to reflect the updated favorites status

    } catch (error) {
      console.error("Error toggling favorite:", error);
    } finally {
      setLoading(false); // Hide loading state
    }
  };
  


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
          onClick={fetchAllBabysitters} // Adjusted to correctly refresh the babysitters list
        >
          Refresh Babysitters List
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
        {babysitters.map(babysitter => (
        <BabysitterCard 
          key={babysitter.id}
          babysitter={babysitter} 
          toggleFavorite={() => toggleFavorite(babysitter.id, babysitter.isFavorite)}
          isFavorite={babysitter.isFavorite} // Ensure this status is correctly determined
        />
      ))}

      </Box>
    </>
  );
};


export default Find;
