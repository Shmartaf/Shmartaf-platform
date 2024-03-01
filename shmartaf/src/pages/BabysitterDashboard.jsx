import Box from "@mui/material/Box";
import humanImage from "../assets/human.png";
import WeeklyStats from "../components/WeeklyStats";
import Tables from "../components/Tables";

const BabysitterDashboard = () => {
  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "row",
        flexGrow: 1,
        width: "100%",
        backgroundColor: "#F8F7F1",
        gap: "20px",
        p: 2,
        height: "100vh",
      }}>
      <Box
        sx={{
          display: "flex",
          flex: 1,
          // backgroundColor: "#Fff",
          border: "1px solid black",
        }}>
        <WeeklyStats />
      </Box>

      <Box
        sx={{
          display: "flex",
          flex: 3,
          backgroundColor: "#Fff",
          border: "1px solid black",
        }}>
        <Tables />
      </Box>
    </Box>
  );
};
export default BabysitterDashboard;
