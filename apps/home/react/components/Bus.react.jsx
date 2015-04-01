var React = require('react');

var Bus = React.createClass({

  render: function() {
    return (
      <div className="bus">
        {this.props.name} with no wheels.
      </div>
    );
  }

});

module.exports = Bus;
