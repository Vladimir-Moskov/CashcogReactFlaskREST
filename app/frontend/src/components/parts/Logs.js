import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getLogs } from "../../actions/logs";
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';

export class Logs extends Component {
    static propTypes = {
        logs: PropTypes.array.isRequired,
        getLogs: PropTypes.func.isRequired
     };

      componentDidMount() {
        this.props.getLogs();
      }

    render(){
        return (
        <div>
            <h2>Logs</h2>
           <BootstrapTable data={ this.props.logs } striped hover condensed pagination version='4'>
              <TableHeaderColumn dataField='id' isKey dataSort={ true }>ID</TableHeaderColumn>
              <TableHeaderColumn dataField='timestamp' dataSort={ true }>TIME</TableHeaderColumn>
              <TableHeaderColumn dataField='remote_addr' dataSort={ true } > ADDRESS</TableHeaderColumn>
              <TableHeaderColumn dataField='url' dataSort={ true }>URL</TableHeaderColumn>
              <TableHeaderColumn dataField='method' dataSort={ true }>METHOD</TableHeaderColumn>
              <TableHeaderColumn dataField='user_agent' dataSort={ true }>AGENT</TableHeaderColumn>
              <TableHeaderColumn dataField='application_type' dataSort={ true }>TYPE</TableHeaderColumn>
            </BootstrapTable>
        </div>
        )
    }
}

const mapStateToProps = state => ({
  logs: state.logs.logs
});

export default connect(
  mapStateToProps,
  { getLogs }
)(Logs);

