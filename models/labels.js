/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('labels', {
    id: {
      autoIncrement: true,
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true
    },
    createdat: {
      type: DataTypes.DATE,
      allowNull: true,
      defaultValue: sequelize.fn('current_timestamp')
    },
    updatedat: {
      type: DataTypes.DATE,
      allowNull: true
    },
    pid: {
      type: DataTypes.STRING(40),
      allowNull: true,
      unique: true
    },
    posneg: {
      type: DataTypes.STRING(10),
      allowNull: true
    }
  }, {
    sequelize,
    tableName: 'labels'
  });
};
