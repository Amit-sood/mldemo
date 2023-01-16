import { useState } from "react";
import Card from "./Card";
import Header from "./MyComponent/Header";
import banner from "./images/banner.jpg";
import Duplicate from "./Duplicate";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import SentimentAnalysis from "./SentimentAnalysis";
import TextSummarization from "./TextSummarization";
import WebScrapping from "./WebScrapping";
import { screenRenderInfo, drawerOptions } from "./constants";

export const Home = () => {
  const [demostate, setDemostate] = useState("");
  const [menuOption, setMenuOption] = useState("Dashboard");

  const demoHandler = (data) => {
    if (data == "") {
      setDemostate("");
    }
    if (data == "Sentiment Analysis") {
      setDemostate("demostate");
    }
    if (data == "Text Summarization") {
      setDemostate("demostate1");
    }
    if (data == "Web Scrapping") {
      setDemostate("demostate2");
    }
    if (data == "Matching & Pinning") {
      setDemostate("demostate3");
    }
  };

  const menuClick = (menuTitle) => {
    setMenuOption(menuTitle);
    setDemostate("");
  };

  const renderHomeCards = () => (
    <>
      {screenRenderInfo.map((item) => {
        const { drawerOptions, iconName, title, description } = item;
        return (
          <>
            {menuOption === drawerOptions && (
              <Card
                icon={iconName}
                onDemoClick={() => demoHandler(title)}
                link="/duplicate"
                title={title}
                description={description}
              />
            )}
          </>
        );
      })}
    </>
  );

  const renderHomeContent = () => (
    <div className="card">
      {demostate === "demostate" ? (
        <SentimentAnalysis />
      ) : demostate === "demostate1" ? (
        <TextSummarization />
      ) : demostate === "demostate2" ? (
        <WebScrapping />
      ) : demostate === "demostate3" ? (
        <Duplicate />
      ) : (
        renderHomeCards()
      )}
    </div>
  );

  return (
    <div>
      <Header title={"My Todo List"} searchBar={false} />
      <div className="banner">
        <img src={banner}></img>
        <div className="overlay">
          <h1>Artificial Intelligence Experience Hub</h1>
        </div>
      </div>
      <div className="content">
        <div className="tabs-v">
          {drawerOptions.map((item, index) => {
            const className = `faHouse${index+1}`
            return (
              <>
                <input
                  id={`rad${index + 1}`}
                  name="rad"
                  type="radio"
                  checked={menuOption === item.name}
                />
                <label
                  data-text={item.name}
                  id={`rad${index + 1}`}
                  onClick={() => menuClick(item.name)}
                ></label>
                <span></span>
                <FontAwesomeIcon icon={item.iconName} className={className}/>
              </>
            );
          })}

          {drawerOptions.map(() => (
            <div className="tab-c">{renderHomeContent()}</div>
          ))}
        </div>
      </div>
    </div>
  );
}