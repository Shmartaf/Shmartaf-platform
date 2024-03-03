import Box from "@mui/material/Box";
import EventsTable from "../components/EventsTable";
import Header from "../components/Header";
import Map from "../components/Map";
import QuickFind from "../components/QuickFind";
import humanImage from "../assets/human.png";
import { useContext } from "react";
import { BabysitterContext } from "../context/BabysitterContext";

const ParentDashboard = () => {
  const { user } = useContext(BabysitterContext).state;
  return (
    <Box sx={{ display: "flex", flexDirection: "column", flexGrow: 1 }}>
      <Header name={user.name} image={humanImage} />
      <EventsTable />
      <QuickFind />
      <Map />
    </Box>
  );
};
export default ParentDashboard;
