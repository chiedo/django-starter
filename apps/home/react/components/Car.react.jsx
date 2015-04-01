var Wheel = require('./Wheel.react.jsx');
var React = require('react');

var Car = React.createClass({

  render: function() {
    return (
      <div className="car" onMouseEnter={this.onMouseEnter}>
        A {this.props.name} with the following wheels
        <ul>
          <li>
            <Wheel />
          </li>
          <li>
            <Wheel />
          </li>
          <li>
            <Wheel />
          </li>
          <li>
            <Wheel />
          </li>
      </ul>
      </div>
    );
  },   
  onMouseEnter: function () {
    console.dir("test");
  },

});

module.exports = Car;
