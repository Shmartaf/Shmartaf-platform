import { Typography } from "@mui/material";
import Box from "@mui/material/Box";
import StarIcon from "@mui/icons-material/Star";

const parentProfile = (props) => {
  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        gap: 1,
        width: "50%",
        height: "50%",
        justifyContent: "start",
        alignItems: "center",
        padding: "10px",
        boxShadow: 2,
        borderRadius: 2,
      }}
    >
      <img src={props.image} style={{ width: "80px", borderRadius: "50%" }} />
      <Box
        sx={{
          display: "flex",
          flexDirection: "row",
          gap: 1,
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <StarIcon sx={{ color: "#5B5CFD" }} />
        <Typography variant="h6">{props?.rating || "4.5"}</Typography>
      </Box>
      <Typography variant="h5" fontWeight={"bold"}>
        {props.name}
      </Typography>
      <Box
        sx={{
          display: "flex",
          flexDirection: "row",
          gap: 1,
          alignItems: "center",
          justifyContent: "center",
        }}
      ></Box>
      <Typography variant="h6" fontWeight={"bold"}>
        {props.location}
      </Typography>
      <Box
        sx={{
          display: "flex",
          flexDirection: "row",
          gap: 1,
          alignItems: "center",
          justifyContent: "center",
          padding: "5px 5px",
        }}
      >
        <Typography>{props.desc}</Typography>
      </Box>
    </Box>
  );
};
export default parentProfile;
