import React, { createContext, useReducer } from "react";

//temp:
const babysitters = [
  {
    name: "Odel Levi",
    image: "https://i.pravatar.cc/300?img=1",
    desc: "Sociable, athletic, loves animals, available frequently, patient.",
    location: "Tel Aviv",
    rating: "4.50",
    isFavorite: true,
    id: 101,
  },
  {
    name: "Shai Damari",
    image: "https://i.pravatar.cc/300?img=2",
    desc: "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    location: "Haifa",
    rating: "4.75",
    isFavorite: true,
    id: 102,
  },
  {
    name: "Nurit Levi",
    image: "https://i.pravatar.cc/300?img=3",
    rating: "3.90",
    desc: "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    isFavorite: true,
    location: "Rishon Lezion",
    id: 103,
  },
  {
    name: "Tom Levi",
    image: "https://i.pravatar.cc/300?img=4",
    rating: "3.50",
    desc: "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    isFavorite: false,
    location: "Holon",
    id: 104,
  },
];
const initialState = {
  items: [],
  selected: {},
  babysitters,
  error: null,
  // userRole: null,
};

const babysitterReducer = (state, action) => {
  switch (action.type) {
    case "SET_BABYSITTERS":
      return { ...state, babysitters: action.payload };

    case "SET_SELECTED":
      return { ...state, selected: action.payload };

    case "CLEAR_SELECTED":
      return { ...state, selected: {} };

    case "ADD_BABYSITTER":
      return { ...state, babysitters: [...state.babysitters, action.payload] };

    case "UPDATE_BABYSITTER":
      return {
        ...state,
        babysitters: state.babysitters.map((item) =>
          item.id === action.payload.id ? action.payload : item,
        ),
        selected: {},
      };

    case "REMOVE_BABYSITTER":
      return {
        ...state,
        babysitters: state.babysitters.filter(
          (item) => item._id !== action.payload,
        ),
        selected: {},
      };

    default:
      return state;
  }
};

const BabysitterContext = createContext();

const BabysitterProvider = ({ children }) => {
  const [state, dispatch] = useReducer(babysitterReducer, initialState);

  return (
    <BabysitterContext.Provider value={{ state, dispatch }}>
      {children}
    </BabysitterContext.Provider>
  );
};

export { BabysitterContext, BabysitterProvider };
