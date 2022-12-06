import { useState } from "react";
import Card from "./Card";
import Header from "./MyComponent/Header";
import banner from "./images/banner.jpg";
import Duplicate from "./Duplicate";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faHouse,
  faWind,
  faChartGantt,
  faShuffle,
  faChartPie,
  faGlobe,
  faEquals,
  faRobot,
} from "@fortawesome/free-solid-svg-icons";
import SentimentAnalysis from "./SentimentAnalysis";
import TextSummarization from "./TextSummarization";
import WebScrapping from "./WebScrapping";

function Home() {
  const [demostate, setDemostate] = useState("");
  const [menuOption, setMenuOption] = useState("Dashboard");

  const demoHandler = (data) => {
    if (data == "") {
      setDemostate("");
    }
    if (data == "sentiment") {
      setDemostate("demostate");
    }
    if (data == "text") {
      setDemostate("demostate1");
    }
    if (data == "web") {
      setDemostate("demostate2");
    }
    if (data == "auto") {
      setDemostate("demostate3");
    }
  };

  const menuClick = (menuTitle) => {
    setMenuOption(menuTitle);
    setDemostate("");
  };

  const renderHomeCards = () => (
    <>
     <Card
        icon={faEquals}
        onDemoClick={() => demoHandler("auto")}
        link="/duplicate"
        title="Matching & Pinning"
        description="Solve duplicate records problem using machine learning in Matching & Pinning Process"
      />
      <Card
        icon={faChartGantt}
        onDemoClick={() => demoHandler("sentiment")}
        link="/duplicate"
        title="Sentiment Analysis"
        description="Understand the sentiment of the customer and make informed business decisions."
      />
      <Card
        icon={faChartPie}
        onDemoClick={() => demoHandler("text")}
        link="/duplicate"
        title="Text Summarization"
        description="Reduce the text size and create a summary of our textual data for business advantage."
      />
      <Card
        icon={faGlobe}
        onDemoClick={() => demoHandler("web")}
        link="/duplicate"
        title="Web Scrapping"
        description="Scrape data from any website at scale and accuracy using best in class open source technology"
      />
     
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
        <img src={banner} ></img>
        <div className="overlay">
          <h1>Artificial Intelligence Experience Hub</h1>
        </div>
      </div>
      <div className="content">
        <div className="tabs-v">
          <input
            id="rad1"
            name="rad"
            type="radio"
            checked={menuOption === "Dashboard"}
          />
          <label
            data-text="Dashboard"
            for="rad1"
            onClick={() => menuClick("Dashboard")}
          ></label>
          <span></span>
          <FontAwesomeIcon icon={faHouse} className="faHouse" />
          <input
            id="rad2"
            name="rad"
            type="radio"
            checked={menuOption === "NLP"}
          />
          <label
            data-text="NLP"
            for="rad2"
            onClick={() => menuClick("NLP")}
          ></label>
          <span></span>
          <FontAwesomeIcon icon={faWind} className="faHouse2" />
          <input
            id="rad3"
            name="rad"
            type="radio"
            checked={menuOption === "Customer Analytics"}
          />
          <label
            data-text="Customer Analytics"
            for="rad3"
            onClick={() => menuClick("Customer Analytics")}
          ></label>
          <span></span>
          <FontAwesomeIcon icon={faChartGantt} className="faHouse3" />
          <input
            id="rad4"
            name="rad"
            type="radio"
            checked={menuOption === "Auto ML"}
          />
          <label
            data-text="Auto ML"
            for="rad4"
            onClick={() => menuClick("Auto ML")}
          ></label>
          <span></span>
          <FontAwesomeIcon icon={faShuffle} className="faHouse4" />
          <input
            id="rad5"
            name="rad"
            type="radio"
            checked={menuOption === "IOT"}
          />
          <label
            data-text="IOT"
            for="rad5"
            onClick={() => menuClick("IOT")}
          ></label>
          <span></span>
          <FontAwesomeIcon icon={faRobot} className="faHouse5" />
          
          <div className="tab-c">{renderHomeContent()}</div>
          <div className="tab-c">{renderHomeContent()}</div>
          <div className="tab-c">{renderHomeContent()}</div>
          <div className="tab-c">{renderHomeContent()}</div>
          <div className="tab-c">{renderHomeContent()}</div>
        </div>
      </div>
    </div>
  );
}

export default Home;
