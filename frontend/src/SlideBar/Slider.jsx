import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import serverip from "../Settings/serverip";
import {
  Sidebar,
  Menu,
  MenuItem,
  SubMenu,
  useProSidebar,
} from "react-pro-sidebar";

const Slider = () => {
  const [URL, setURL] = useState("");
  return (
    <div style={{ display: "flex", height: "100vh" }}>
      <div>
        <Sidebar className="app">
          <Menu>
            <MenuItem className="menu1">
              <h2>AI ToolKit</h2>
            </MenuItem>
            <MenuItem> </MenuItem>

            <MenuItem onClick={() => setURL("chat")}>
              {" "}
              Conversation Generator{" "}
            </MenuItem>
            <MenuItem onClick={() => setURL("code_gen")}>
              {" "}
              Code Generator{" "}
            </MenuItem>

            <MenuItem onClick={() => setURL("video")}>
              {" "}
              Text to Video Generator{" "}
            </MenuItem>
            <MenuItem onClick={() => setURL("image")}>
              {" "}
              Text to Image Generator{" "}
            </MenuItem>
            <MenuItem onClick={() => setURL("audio")}>
              {" "}
              Music Generator{" "}
            </MenuItem>
          </Menu>
        </Sidebar>
      </div>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          flexDirection: "column",
          width: "100%",
        }}
      >
        <h1>Welcome ! </h1>
        {URL && (
          <iframe
            src={serverip.ip + URL}
            frameborder="10"
            style={{ borderRadius: "20px", width: "100vh", height: "80vh" }}
          ></iframe>
        )}
      </div>
    </div>
  );
};

export default Slider;
