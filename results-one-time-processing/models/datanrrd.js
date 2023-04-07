/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('datanrrd', {
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
    id4: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    id7: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    idsha: {
      type: DataTypes.STRING(50),
      allowNull: true
    },
    urlhost0: {
      type: DataTypes.STRING(200),
      allowNull: true
    },
    urldir: {
      type: DataTypes.STRING(200),
      allowNull: true
    },
    urlfnbase: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    pathinserver: {
      type: DataTypes.STRING(500),
      allowNull: true
    },
    urlhost1: {
      type: DataTypes.STRING(200),
      allowNull: true
    }
  }, {
    sequelize,
    tableName: 'datanrrd'
  });
};
