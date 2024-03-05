import React, { useState, useEffect } from "react";
import ContactedListContainer from "../components/ContactedListComponent";
import { Grid, Typography } from "@mui/material";
import { useAuth } from "../AuthContext";
import { get } from "../api";
const Contacted = () => {
  const [contacted, setContacted] = useState([]);
  const { user } = useAuth();

  const fetchContacted = async () => {
    if (user.userData?.userType === "parent") {
      const parent = await get("parents", user.id);
      console.log("parent:", parent);
      const contacted = parent.contacted;
      console.log("contacted:", contacted);
      setContacted(contacted);
    } else {
      const babysitter = await get("babysitters", user.id);
      console.log("babysitter:", babysitter);
      const contacted = babysitter.contacted;
      console.log("contacted:", contacted);
      setContacted(contacted);
    }
  };

  useEffect(() => {
    if (user && contacted.length === 0) {
      fetchContacted();
      console.log("contacted:", contacted);
    }
  });
  return (
    <div>
      <h1>Contacted</h1>
      <Grid container spacing={2}>
        {contacted.map((item) => (
          <Grid item key={item.id} xs={4} sm={4} md={2} lg={2}>
            {/* Adjust the Grid item sizes based on your layout needs */}
            <ContactedListContainer contactedData={contacted} />
          </Grid>
        ))}
      </Grid>
    </div>
  );
};
export default Contacted;
