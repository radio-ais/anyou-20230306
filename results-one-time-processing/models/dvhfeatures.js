/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('dvhfeatures', {
    id: {
      autoIncrement: true,
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true
    },
    id4: {
      type: DataTypes.STRING(10),
      allowNull: true,
      unique: true
    },
    id7: {
      type: DataTypes.STRING(10),
      allowNull: true,
      unique: true
    },
    LV05: {
      type: DataTypes.STRING(20),
      allowNull: true,
      comment: 'of whole lung'
    },
    LV10: {
      type: DataTypes.STRING(20),
      allowNull: true,
      comment: 'of whole lung'
    },
    LV20: {
      type: DataTypes.STRING(20),
      allowNull: true,
      comment: 'of whole lung'
    },
    LV30: {
      type: DataTypes.STRING(20),
      allowNull: true,
      comment: 'of whole lung'
    },
    LV40: {
      type: DataTypes.STRING(20),
      allowNull: true,
      comment: 'of whole lung'
    },
    maxdosew: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    meandosew: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    mediandosew: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    volumew: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    maxdosep: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    meandosep: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    mediandosep: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    volumep: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    filename: {
      type: DataTypes.STRING(500),
      allowNull: true
    },
    isdifferential: {
      type: DataTypes.STRING(10),
      allowNull: true,
      comment: '1: is differential , 0: not differential'
    }
  }, {
    sequelize,
    tableName: 'dvhfeatures'
  });
};
