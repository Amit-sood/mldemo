import "./duplicate.css";
import React, { useState } from "react";
import * as XLSX from "xlsx";
import axios from 'axios';


function Duplicate(props) {
  const [columns, setColumns] = useState([]); //optional for now 
  const [data, setData] = useState([]);

  const[fullName, setFullName] = useState([]);
  const[firstName, setFirstName] = useState([]);
  const[lastName, setLastName] = useState([]);
  const[address, setAddress] = useState([]);
  const[phone, setPhone] = useState([]);
  const[postCode, setPostCode] = useState([]);

  const [responseData, setResponseData] = useState();
  const [isLoading, setIsLoading] = useState(false);
  const [err, setErr] = useState('');
  


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

    // prepare columns list from headers
    //optional for now !!
    const columns = headers.map((c) => ({
      name: c,
      selector: c,
    }));

    setData(list);
    setColumns(columns);
    console.log(list);
  };
  let reqData= "";

    reqData =reqData+" "+fullName+" "+firstName+" "+lastName+" "+address+" "+postCode+" "+phone;
  
    
 
  const handleClick = async () => {

    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:5000/mandp', {
        method: 'POST',
        body: JSON.stringify({"data":{reqData}}),
        headers: {
          'Content-Type': 'text/plain'
        },
      });
      // var response;
      // axios.post(`http://localhost:5000/mandp`, { reqData })
      // .then(response => {
      //   console.log(response);
      //   console.log(response.data);
      // })
      if (!response.ok) {
        throw new Error(`Error! status: ${response.status}`);
      }

      // const result = await response.json();
      setResponseData(await response.json());
      console.log('request:', reqData);
      console.log('result is: ', JSON.stringify(responseData, null, 4));

    } catch (err) {
      setErr(err.message);
    } finally {
      setIsLoading(false);
      console.log('response:'+responseData.score);
    }
 
var newObj=[{}];
responseData.results.forEach((element, index) => {
  // obj[element] = responseData.score[index];
  // console.log('obj:'+responseData.result[element]);

  newObj.push({element: element, score: responseData.score[index]});
  console.log(newObj);
});


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
                
                <select onChange={e => setFullName(e.target.value)
                }>
                  <option>Selct Full Name</option>
                  {data.map((option) => (
                    <option value={option["Full Name"]}>
                      {option["Full Name"]}
                    </option>
                  ))}
                </select>
                <select onChange={e => setFirstName(e.target.value) }>
                  <option>Selct First Name</option>
                  {data.map((option) => (
                    <option value={option["First Name"]}>
                      {option["First Name"]}
                    </option>
                  ))}
                </select>

                <select onChange={e => setLastName(e.target.value) }>
                  <option >Selct Last Name</option>
                  {data.map((option) => (
                    <option value={option["Last Name"]}>
                      {option["Last Name"]}
                    </option>
                  ))}
                </select>

                <select onChange={e => setAddress(e.target.value) }>
                  <option>Select Address</option>
                  {data.map((option) => (
                    <option value={option.Address}>{option.Address}</option>
                  ))}
                </select>

                <select onChange={e => setPhone(e.target.value) }>
                  <option>Selct Phone</option>
                  {data.map((option) => (
                    <option value={option["Phone number"]}>
                      {option["Phone number"]}
                    </option>
                  ))}
                </select>

                <select onChange={e => setPostCode(e.target.value) }>
                  <option>Selct Postcode</option>
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
                  placeholder="Enter Name"
                />
                <input
                  name="file-upload-field"
                  type="text"
                  className="input"
                  placeholder="Enter First Name"
                />
                <input
                  name="file-upload-field"
                  type="text"
                  className="input"
                  placeholder="Enter Last Name"
                />
                <input
                  name="file-upload-field"
                  type="text"
                  className="input"
                  placeholder="Enter Address "
                />
                <input
                  name="file-upload-field"
                  type="text"
                  className="input"
                  placeholder="Enter Phone"
                />
                <input
                  name="file-upload-field"
                  type="text"
                  className="input"
                  placeholder="Enter Postcode"
                />
              </div>
              <div className="bottom">
                <button>Reset</button>
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
             
              <tr>
                <td data-th="Supplier Code">32</td>
                <td data-th="Supplier Name">4%</td>
              </tr>
              <tr>
                <td data-th="Supplier Code">32</td>
                <td data-th="Supplier Name">4%</td>
              </tr>
              <tr>
                <td data-th="Supplier Code">32</td>
                <td data-th="Supplier Name">4%</td>
              </tr>
              <tr>
                <td data-th="Supplier Code">32</td>
                <td data-th="Supplier Name">4%</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
}

export default Duplicate;
