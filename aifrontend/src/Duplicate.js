import "./duplicate.css";
import React, { useState } from "react";
import * as XLSX from "xlsx";
import Popup from 'reactjs-popup';
import Table from 'react-bootstrap/Table'
import { useEffect } from "react";
import {  Backdrop ,CircularProgress } from '@mui/material';
// import ReactTable from "react-table";  


function Duplicate(props) {
  
  const [data, setData] = useState([]);

  const[fullName, setFullName] = useState([]);
  const[firstName, setFirstName] = useState([]);
  const[lastName, setLastName] = useState([]);
  const[address, setAddress] = useState([]);
  const[phone, setPhone] = useState([]);
  const[postCode, setPostCode] = useState([]);

  const [responseData, setResponseData] = useState({results:[], score:[]});
  const [isLoading, setIsLoading] = useState(false);
  const [err, setErr] = useState('');
  let result ;
 
  const [best,setBest] = useState([]);
  const [good,setGood] = useState([]);
  const [average,setAverage] = useState([]);
  const [poor,setPoor] = useState([]);
  const [btnClick,setBtnClick]= useState();
  const [reqData,setReqData] = useState("");
  const columns = [{  
    Header: 'Data',  
    accessor: 'data'  
   },{  
   Header: 'Score',  
   accessor: 'score'  
   }]  ;

  const handleFileUpload = (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();
    reader.onload = (evt) => {
      /* Parse data */
      const bstr = evt.target.result;
      const wb = XLSX.read(bstr, { type: "binary" });
      /* Get first worksheet */
      const wsname = wb.SheetNames[0];
      const ws = wb.Sheets[wsname];
      /* Convert array of arrays */
      const data = XLSX.utils.sheet_to_csv(ws, { header: 1 });
      processData(data);
    };
    reader.readAsBinaryString(file);
  };
  const processData = (dataString) => {
    const dataStringLines = dataString.split(/\r\n|\n/);
    const headers = dataStringLines[0].split(
      /,(?![^"]*"(?:(?:[^"]*"){2})*[^"]*$)/,
    );

    const list = [];
    for (let i = 1; i < dataStringLines.length; i++) {
      const row = dataStringLines[i].split(
        /,(?![^"]*"(?:(?:[^"]*"){2})*[^"]*$)/,
      );
      if (headers && row.length == headers.length) {
        const obj = {};
        for (let j = 0; j < headers.length; j++) {
          let d = row[j];
          if (d.length > 0) {
            if (d[0] == '"') d = d.substring(1, d.length - 1);
            if (d[d.length - 1] == '"') d = d.substring(d.length - 2, 1);
          }
          if (headers[j]) {
            obj[headers[j]] = d;
          }
        }

        // remove the blank rows
        if (Object.values(obj).filter((x) => x).length > 0) {
          list.push(obj);
        }
      }
    }

    setData(list);

    console.log(list);
  };
 
  
    
    const handleReset =()=>{

      
      window.location.reload(false);

      console.log("Request:"+reqData);
    console.log('result is: ', JSON.stringify(responseData, null, 4));
    };
   
 
    useEffect(()=>{
      
        setReqData(fullName+" "+firstName+" "+lastName+" "+address+" "+postCode+" "+phone);
        console.log("ReqData:"+reqData);
       
    },[fullName,firstName,lastName,address,phone,postCode,btnClick]);
  useEffect(()=>{
    console.log("Request:"+reqData);
    console.log('result is: ', JSON.stringify(responseData, null, 4));

    var newObj=[];
responseData.results.forEach((element, index) => {


  newObj.push({data: element,score: responseData.score[index]});
  newObj.sort((a,b)=>b.score - a.score);
  
});


newObj.forEach(obj=>{
  if(obj.score >0.90)
  {
    setBest(best=>[...best,obj]);
  }
  else if(obj.score >0.75)
  {
    setGood(good=>[...good,obj]);
  }
  else if(obj.score >0.60)
  {
    setAverage(average=>[...average,obj]);
  }
  else
  {
    setPoor(poor=>[...poor,obj]);
  }
});

  },[responseData]);
    
  const handleClick = async () => {
    setBtnClick(!btnClick);
    setBest([]);
    setGood([]);
    setAverage([]);
    setPoor([]);

    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:5000/mandp', {
        method: 'POST',
        body: JSON.stringify({"data":reqData}),
        headers: {
          'Content-Type': 'text/plain'
        }
      });

      if (!response.ok) {
        throw new Error(`Error! status: ${response.status}`);
      }

      result = await response.json();

    } catch (err) {
      setErr(err.message);
    } finally {
      setIsLoading(false);
      setResponseData(result);
        
    }
  };
  return (
    <>
      <h1 className="duplicateHeading">
        Duplicate Records Detector Through Machine Learning - Proof Of Concept
      </h1>
      <div className="duplicateBox">
        <div className="left">
          <div className="content">
            <div className="header">
              <input
                type="file"
                accept=".csv,.xlsx,.xls"
                onChange={handleFileUpload}
              />
              <button>Find Duplicates With Selected % Accuracy</button>
              <button>%</button>
              <button>All or Top count</button>
            </div>
            <div className="leftContent">
              <div className="selectBox">
                <h5>Select From The Data Uploaded </h5>
                
                <select onChange={e => {setFullName(e.target.value);
                }
                
                }>

                  <option value={""}>Selct Full Name</option>
                  {data.map((option) => (
                    <option value={option["Full Name"]}>
                      {option["Full Name"]}
                    </option>
                  ))}
                </select>
                <select onChange={e => setFirstName(e.target.value) }>

                  <option value={""}>Selct First Name</option>

                  {data.map((option) => (
                    <option value={option["First Name"]}>
                      {option["First Name"]}
                    </option>
                  ))}
                </select>

                <select onChange={e => setLastName(e.target.value) }>

                  <option value={""}>Selct Last Name</option>

                  {data.map((option) => (
                    <option value={option["Last Name"]}>
                      {option["Last Name"]}
                    </option>
                  ))}
                </select>

                <select onChange={e => setAddress(e.target.value) }>

                  <option value={""}>Select Address</option>

                  {data.map((option) => (
                    <option value={option.Address}>{option.Address}</option>
                  ))}
                </select>

                <select onChange={e => setPhone(e.target.value) }>

                  <option value={""}>Selct Phone</option>

                  {data.map((option) => (
                    <option value={option["Phone number"]}>
                      {option["Phone number"]}
                    </option>
                  ))}
                </select>

                <select onChange={e => setPostCode(e.target.value) }>

                  <option value={""}>Selct Postcode</option>

                  {data.map((option) => (
                    <option value={option["Postcode"]}>
                      {option["Postcode"]}
                    </option>
                  ))}
                </select>

              </div>
            </div>
            <div className="rightContent">
              <h5>Or Enter Record to detect duplicity: </h5>
              <div className="inputBox">
                <input
                  name="file-upload-field"
                  type="text"
                  className="input"

                  placeholder="Enter Name" onChange={e => setFullName(e.target.value) }

                />
                <input
                  name="file-upload-field"
                  type="text"
                  className="input"

                  placeholder="Enter First Name" onChange={e => setFirstName(e.target.value) }

                />
                <input
                  name="file-upload-field"
                  type="text"
                  className="input"

                  placeholder="Enter Last Name" onChange={e => setLastName(e.target.value) }

                />
                <input
                  name="file-upload-field"
                  type="text"
                  className="input"

                  placeholder="Enter Address " onChange={e => setAddress(e.target.value) }

                />
                <input
                  name="file-upload-field"
                  type="text"
                  className="input"

                  placeholder="Enter Phone" onChange={e => setPhone(e.target.value) }

                />
                <input
                  name="file-upload-field"
                  type="text"
                  className="input"

                  placeholder="Enter Postcode" onChange={e => setPostCode(e.target.value) }

                />
              </div>
              <div className="bottom">
                <button onClick={handleReset}>Reset</button>
                <button onClick={handleClick}>Detect</button>
              </div>
            </div>
          </div>
        </div>
        <div className="right">
          <h5>Outcome</h5>
          <table className="rwd-table">
            <tbody>
              <tr>
                <th>Record Found</th>
                <th>Accuracy %</th>
              </tr>
             
              {/* <tr> */}
              <tr>
              <Popup trigger={<td data-th="Supplier Code"  ><span> {best.length}</span></td>}
            
            modal nested scroll
              
     position="right center">
       <div ><Table  stripped bordered hover responsive variant="dark" size="sm">
  <thead>
    <tr>
      <th>Data</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    {best.map(item => {
      return (
        <tr key={item.data}>
          <td>{ item.data }</td>
          <td>{ item.score*100+"%" }</td>
        </tr>
      );
    })}
  </tbody>
</Table></div>
      
    </Popup>
                <td data-th="Supplier Name">{">90%"}</td>
              </tr>
              <tr>
              <Popup trigger={<td data-th="Supplier Code"  ><span> {good.length}</span></td>}
            
            modal nested scroll
              
     position="right center">
       <div ><Table  stripped bordered hover responsive variant="dark" size="sm">
  <thead>
    <tr>
      <th>Data</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    {good.map(item => {
      return (
        <tr key={item.data}>
          <td>{ item.data }</td>
          <td>{ item.score*100+"%" }</td>
        </tr>
      );
    })}
  </tbody>
</Table></div>
      
    </Popup>
                <td data-th="Supplier Name">{"90% - 75%"}</td>
              </tr>
              <tr>
              <Popup trigger={<td data-th="Supplier Code"  ><span> {average.length}</span></td>}
            
            modal nested scroll
              
     position="right center">
       <div ><Table  stripped bordered hover responsive variant="dark" size="sm">
  <thead>
    <tr>
      <th>Data</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    {average.map(item => {
      return (
        <tr key={item.data}>
          <td>{ item.data }</td>
          <td>{ item.score*100+"%" }</td>
        </tr>
      );
    })}
  </tbody>
</Table></div>
      
    </Popup>
                <td data-th="Supplier Name">{"75% - 60%"}</td>
              </tr>
              <tr>
              <Popup trigger={<td data-th="Supplier Code"  ><span> {poor.length}</span></td>}
            
            modal nested scroll
              
     position="right center">
       <div ><Table  stripped bordered hover responsive variant="dark" size="sm">
  <thead>
    <tr>

      <th>User</th>
      <th>Score (%)</th>

    </tr>
  </thead>
  <tbody>
    {poor.map(item => {
      return (
        <tr key={item.data}>
          <td>{ item.data }</td>

          <td>{ item.score*100  }</td>

        </tr>
      );
    })}
  </tbody>
</Table></div>
      
    </Popup>
                <td data-th="Supplier Name">{"<60%"}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
  <Backdrop  sx={{ color: '#fff', zIndex: (theme) => theme.zIndex.drawer + 1 }} open={isLoading} >
          <CircularProgress color="inherit" />
      </Backdrop>
    </>
  );
}

export default Duplicate;
