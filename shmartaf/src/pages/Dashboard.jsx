import Box from "@mui/material/Box";
import EventsTable from "../components/EventsTable";
import Header from "../components/Header";
import Map from "../components/Map";
import QuickFind from "../components/QuickFind";
import humanImage from "../assets/human.png";

const Dashboard = () => {
  return (
    <Box sx={{ display: "flex", flexDirection: "column", flexGrow: 1 }}>
      <Header name="Nurit Levi" image={humanImage} />
      <EventsTable />
      <QuickFind />
      <Map />
    </Box>
  );
};
export default Dashboard;
